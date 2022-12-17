/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
// const colors = require('tailwindcss/colors')
const { fontFamily, screens } = require("tailwindcss/defaultTheme");

module.exports = {
  mode: "jit",
  content: [
    "../templates/**/*.html",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
  ],
  darkMode: "class", // or 'media' or 'class'
  theme: {
    screens: {
      xxs: "270px",
      xs: "350px",
      ...screens,
    },
    extend: {
      fontFamily: {
        sans: ["Barlow", ...fontFamily.sans],
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    // require("@tailwindcss/aspect-ratio"),
    require("tailwind-scrollbar-hide"),
  ],
};
