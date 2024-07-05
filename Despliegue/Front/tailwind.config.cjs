/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        grayScale: {
          2: '#EFEFEF',
          3: '#C4C4C4',
          6: '#353434',
        },
        purple: '#772583',
        primary: '#672779',
        primary02: '#E0D1FF',
        secondary: '#521F61',
        secondary01: '#F3F1F6',
        secondary02: '#E3DFEA',
        secondary03: '#B0A3C4',
        secondary04: '#9C73A8',
        secondary05: '#A90061',
        secondary06: '#E1251B',
        secondary07: '#777676',
        secondary08: '#3BC392',
        secondary09: '#C4C4C4',
        secondary10: '#F6F6F6',
        gradient:
          'linear-gradient(135deg, #EE2737 14.64%, #BC0075 49.99%, #772583 85.36%)',
        sidebar: 'rgb(255, 255, 255, 0.1)',
        status01:'#D34DE2',
        status02:'#038356',
        status03:'#E1251B',
        status04:'#FFC83E',
        status05:'#6436AB',
      }
    },
  },
  plugins: [],
};
