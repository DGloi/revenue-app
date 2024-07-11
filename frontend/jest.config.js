module.exports = {
  roots: ['<rootDir>/src'],
  transform: {
    '^.+\\.(js|jsx)$': 'babel-jest',
  },
  testRegex: '(/__tests__/.*|(\\.|/)(test|spec))\\.jsx?$',
  moduleFileExtensions: ['js', 'jsx', 'json', 'node'],
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  transformIgnorePatterns: [
    "[/\\\\]node_modules[/\\\\](?!react-dnd|dnd-core|@react-dnd).+\\.(js|jsx|mjs|cjs|ts|tsx)$",
    "^.+\\.module\\.(css|sass|scss)$"
  ],
  moduleNameMapper: {
    '\\.(css|less|sass|scss)$': 'identity-obj-proxy',
    '\\.svg$': 'jest-transform-stub',
    '\\.(jpg|jpeg|png|gif|webp|avif|mp4|mp3|wav|ogg|ttf|woff|woff2)$': 'jest-transform-stub'
  },
  testEnvironment: 'jsdom',
};