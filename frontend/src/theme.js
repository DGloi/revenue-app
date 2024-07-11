// src/theme.js
export const lightThemeColors = {
    primary: '#00a4f7',
    secondary: '#fff',
    text: '#000',
    background: '#fff',
  };
  
  export const darkThemeColors = {
    primary: '#333',
    secondary: '#555',
    text: '#fff',
    background: '#000',
  };
  
  export const getThemeColors = (mode) => (mode === 'dark' ? darkThemeColors : lightThemeColors);