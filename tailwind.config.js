/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './content/**/*.{html,md}',
    './layouts/**/*.html',
    './themes/PaperMod/layouts/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        'farsi': ['Vazir', 'Tahoma', 'Arial', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@01sadra/tailwind-neobrutalism')({
      // Enable RTL support
      rtl: true,
      // Use Persian/Farsi font
      fontFamily: {
        'farsi': ['Vazir', 'Tahoma', 'Arial', 'sans-serif'],
      }
    })
  ],
}