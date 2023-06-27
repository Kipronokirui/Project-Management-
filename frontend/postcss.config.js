// module.exports = {
//   content: [
//     "./pages/**/*.{ts,tsx}",
//     "./public/**/*.html",
//   ],
//   plugins: {
//     tailwindcss: {},
//     autoprefixer: {},
//   },
// }
module.exports = {
  content: [
    "./node_modules/flowbite-react/**/*.js",
    "./pages/**/*.{js, jsx, ts,tsx}",
    "./public/**/*.html",
  ],
  plugins: [
    require("flowbite/plugin")
  ],
  theme: {},
};
