/** @type {import('tailwindcss').Config} */

const colors = require('tailwindcss/colors')

module.exports = {
    content: [
        "../templates/*.{html,js}",
        "../templates/**/*.{html,js}",
        "../templates/**/**/*.{html,js}",
        "../apps/resources/enums/*.py",
        "./src/*.{js,jsx,ts,tsx}",
        "./src/components/*.{js,jsx,ts,tsx}",
        "./src/components/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
        colors: {
            current: 'currentColor',
            transparent: 'transparent',
            white: '#FFFFFF',
            black: '#000000',
            gray: colors.gray,
            slate: colors.slate,
            green: colors.green,
            red: colors.red,
            pink: colors.pink,
            blue: colors.blue,
            sky: colors.sky,
            yellow: colors.yellow,
            djs: {
                'primary': '#E7FE55',
                'secondary': '#e83902'
            }
        },
        extend: {},
    },
    plugins: [],
}

