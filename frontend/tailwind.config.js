/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#1E88E5',
          foreground: '#ffffff',
          dark: '#1565C0',
          muted: '#E3F2FD',
        },
        accent: {
          DEFAULT: '#FFB300',
          dark: '#FF8F00',
        },
        surface: {
          DEFAULT: '#F8FAFC',
          card: '#FFFFFF',
          border: '#E2E8F0',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        card: '0 10px 15px -3px rgba(15, 23, 42, 0.1)',
      },
    },
  },
  plugins: [],
}
