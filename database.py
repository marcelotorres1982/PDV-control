"""
Módulo de gerenciamento de dados local
"""

import json
from pathlib import Path
from datetime import datetime

class Database:
    """Classe para gerenciar banco de dados local em JSON"""
    
    def __init__(self, db_path='data/local_backup.json'):
        self.db_path = Path(db_path)
        self._ensure_data_dir()
        self._load_data()
    
    def _ensure_data_dir(self):
        """Garante que o diretório de dados existe"""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        if not self.db_path.exists():
            self._save_data([])
    
    def _load_data(self):
        """Carrega dados do arquivo JSON"""
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                self.records = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.records = []
            self._save_data(self.records)
    
    def _save_data(self, data):
        """Salva dados no arquivo JSON"""
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def add_record(self, registro):
        """
        Adiciona um novo registro
        
        Args:
            registro: Dicionário com os dados do registro
            
        Returns:
            ID do registro adicionado
        """
        # Adiciona timestamp único como ID
        registro['id'] = f"{registro['data']}_{registro['hora']}_{registro['promotor']}".replace(':', '-').replace(' ', '_')
        registro['created_at'] = datetime.now().isoformat()
        
        self.records.append(registro)
        self._save_data(self.records)
        
        return registro['id']
    
    def get_record_by_id(self, record_id):
        """
        Busca um registro por ID
        
        Args:
            record_id: ID do registro
            
        Returns:
            Dicionário com os dados ou None
        """
        for record in self.records:
            if record.get('id') == record_id:
                return record
        return None
    
    def get_all_records(self):
        """
        Retorna todos os registros
        
        Returns:
            Lista de registros
        """
        return self.records.copy()
    
    def get_records_by_date(self, date_str):
        """
        Busca registros por data
        
        Args:
            date_str: Data no formato YYYY-MM-DD
            
        Returns:
            Lista de registros
        """
        return [r for r in self.records if r.get('data') == date_str]
    
    def get_records_by_promotor(self, promotor):
        """
        Busca registros por promotor
        
        Args:
            promotor: Nome do promotor
            
        Returns:
            Lista de registros
        """
        return [r for r in self.records if r.get('promotor') == promotor]
    
    def get_records_by_pdv(self, pdv):
        """
        Busca registros por PDV
        
        Args:
            pdv: Nome do PDV
            
        Returns:
            Lista de registros
        """
        return [r for r in self.records if r.get('pdv') == pdv]
    
    def get_records_by_date_range(self, start_date, end_date):
        """
        Busca registros por intervalo de datas
        
        Args:
            start_date: Data inicial (YYYY-MM-DD)
            end_date: Data final (YYYY-MM-DD)
            
        Returns:
            Lista de registros
        """
        return [
            r for r in self.records 
            if start_date <= r.get('data', '') <= end_date
        ]
    
    def update_record(self, record_id, updated_data):
        """
        Atualiza um registro existente
        
        Args:
            record_id: ID do registro
            updated_data: Dicionário com os dados atualizados
            
        Returns:
            True se atualizado, False se não encontrado
        """
        for i, record in enumerate(self.records):
            if record.get('id') == record_id:
                self.records[i].update(updated_data)
                self.records[i]['updated_at'] = datetime.now().isoformat()
                self._save_data(self.records)
                return True
        return False
    
    def delete_record(self, record_id):
        """
        Remove um registro
        
        Args:
            record_id: ID do registro
            
        Returns:
            True se removido, False se não encontrado
        """
        for i, record in enumerate(self.records):
            if record.get('id') == record_id:
                self.records.pop(i)
                self._save_data(self.records)
                return True
        return False
    
    def get_statistics(self):
        """
        Retorna estatísticas gerais
        
        Returns:
            Dicionário com estatísticas
        """
        if not self.records:
            return {
                'total_registros': 0,
                'total_promotores': 0,
                'total_pdvs': 0,
                'total_deslocamento': 0,
                'total_entradas': 0,
                'total_fotos': 0
            }
        
        promotores = set(r.get('promotor') for r in self.records)
        pdvs = set(r.get('pdv') for r in self.records)
        total_deslocamento = sum(r.get('valor_deslocamento', 0) for r in self.records)
        total_entradas = sum(r.get('num_entradas', 1) for r in self.records)
        total_fotos = sum(len(r.get('fotos', [])) for r in self.records)
        
        return {
            'total_registros': len(self.records),
            'total_promotores': len(promotores),
            'total_pdvs': len(pdvs),
            'total_deslocamento': total_deslocamento,
            'total_entradas': total_entradas,
            'total_fotos': total_fotos,
            'promotores': list(promotores),
            'pdvs': list(pdvs)
        }
    
    def get_promotor_statistics(self, promotor):
        """
        Retorna estatísticas de um promotor específico
        
        Args:
            promotor: Nome do promotor
            
        Returns:
            Dicionário com estatísticas
        """
        registros = self.get_records_by_promotor(promotor)
        
        if not registros:
            return {
                'total_visitas': 0,
                'total_deslocamento': 0,
                'total_entradas': 0,
                'total_fotos': 0,
                'pdvs_visitados': []
            }
        
        pdvs = set(r.get('pdv') for r in registros)
        total_deslocamento = sum(r.get('valor_deslocamento', 0) for r in registros)
        total_entradas = sum(r.get('num_entradas', 1) for r in registros)
        total_fotos = sum(len(r.get('fotos', [])) for r in registros)
        
        return {
            'total_visitas': len(registros),
            'total_deslocamento': total_deslocamento,
            'total_entradas': total_entradas,
            'total_fotos': total_fotos,
            'pdvs_visitados': list(pdvs)
        }
    
    def export_to_csv(self, output_path='data/export.csv'):
        """
        Exporta dados para CSV
        
        Args:
            output_path: Caminho do arquivo de saída
        """
        import csv
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            if not self.records:
                return
            
            # Cabeçalhos
            fieldnames = ['data', 'hora', 'promotor', 'pdv', 'valor_deslocamento', 
                         'num_entradas', 'observacoes', 'num_fotos']
            
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            # Dados
            for record in self.records:
                row = {
                    'data': record.get('data', ''),
                    'hora': record.get('hora', ''),
                    'promotor': record.get('promotor', ''),
                    'pdv': record.get('pdv', ''),
                    'valor_deslocamento': record.get('valor_deslocamento', 0),
                    'num_entradas': record.get('num_entradas', 1),
                    'observacoes': record.get('observacoes', ''),
                    'num_fotos': len(record.get('fotos', []))
                }
                writer.writerow(row)
    
    def clear_all_records(self):
        """Remove todos os registros (use com cuidado!)"""
        self.records = []
        self._save_data(self.records)
    
    def backup_database(self, backup_path='data/backup'):
        """
        Cria um backup do banco de dados
        
        Args:
            backup_path: Diretório para salvar o backup
        """
        backup_dir = Path(backup_path)
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = backup_dir / f'backup_{timestamp}.json'
        
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(self.records, f, indent=2, ensure_ascii=False)
        
        return str(backup_file)