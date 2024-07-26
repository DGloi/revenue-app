import React, { useState, useMemo } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import Header from './components/header';
import Sidebar from './components/sidebar';

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [dateRange, setDateRange] = useState({ startDate: new Date(), endDate: new Date() });

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: darkMode ? 'dark' : 'light',
        },
      }),
    [darkMode]
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <DndProvider backend={HTML5Backend}>
          <Header darkMode={darkMode} setDarkMode={setDarkMode} setDateRange={setDateRange} />
          <Sidebar darkMode={darkMode} setDarkMode={setDarkMode} />
          <Routes>

          </Routes>
        </DndProvider>
      </Router>
    </ThemeProvider>
  );
}

export default App;