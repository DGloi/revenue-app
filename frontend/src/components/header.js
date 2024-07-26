import React, { useState } from 'react';
import { AppBar, Toolbar, IconButton, Box, Menu, MenuItem, Button, Typography } from '@mui/material';
import { styled, useTheme } from '@mui/system';
import { Brightness4, Brightness7, CalendarToday } from '@mui/icons-material';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { getThemeColors } from '../theme';

const HeaderBar = styled(AppBar)`
  background-color: ${(props) => getThemeColors(props.theme.palette.mode).primary};
  height: 70px;
  justify-content: center;
  z-index: 1100; /* Ensure the header is below the sidebar */
  position: relative;
`;

const HeaderContent = styled(Toolbar)`
  display: flex;
  justify-content: space-between;
`;

const DateRangePickerButton = styled(Button)`
  color: ${(props) => getThemeColors(props.theme.palette.mode).text};
  border-color: ${(props) => getThemeColors(props.theme.palette.mode).text};
`;

const CustomDatePicker = styled(DatePicker)`
  .react-datepicker {
    background-color: ${(props) => getThemeColors(props.theme.palette.mode).background};
    border: none;
  }
  .react-datepicker__header {
    background-color: ${(props) => getThemeColors(props.theme.palette.mode).primary};
  }
  .react-datepicker__current-month,
  .react-datepicker__day-name,
  .react-datepicker__day {
    color: ${(props) => getThemeColors(props.theme.palette.mode).text};
  }
  .react-datepicker__day--selected {
    background-color: ${(props) => getThemeColors(props.theme.palette.mode).secondary};
  }
`;

const Header = ({ darkMode, setDarkMode, setDateRange }) => {
  const theme = useTheme();
  const [anchorEl, setAnchorEl] = useState(null);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());

  const handleThemeChange = () => {
    setDarkMode(!darkMode);
  };

  const handleOpenMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setAnchorEl(null);
  };

  const handleMenuClick = (range) => {
    const today = new Date();
    if (range === 'last_week') {
      setStartDate(new Date(today.getFullYear(), today.getMonth(), today.getDate() - 7));
      setEndDate(today);
    } else if (range === 'last_month') {
      setStartDate(new Date(today.getFullYear(), today.getMonth() - 1, today.getDate()));
      setEndDate(today);
    } else if (range === 'year_to_date') {
      setStartDate(new Date(today.getFullYear(), 0, 1));
      setEndDate(today);
    }
    handleCloseMenu();
    setDateRange({ startDate, endDate });
  };

  const iconColor = getThemeColors(theme.palette.mode).text;

  return (
    <HeaderBar position="static" theme={theme}>
      <HeaderContent>
        <Typography variant="h6" color="inherit"></Typography>
        <Box>
          <DateRangePickerButton
            variant="outlined"
            startIcon={<CalendarToday />}
            onClick={handleOpenMenu}
          >
            Pick Date Range
          </DateRangePickerButton>
          <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={handleCloseMenu}
          >
            <MenuItem onClick={() => handleMenuClick('last_week')}>Last Week</MenuItem>
            <MenuItem onClick={() => handleMenuClick('last_month')}>Last Month</MenuItem>
            <MenuItem onClick={() => handleMenuClick('year_to_date')}>Year to Date</MenuItem>
            <MenuItem onClick={() => handleMenuClick('custom')}>
              <CustomDatePicker
                selected={startDate}
                onChange={(date) => setStartDate(date)}
                selectsStart
                startDate={startDate}
                endDate={endDate}
                inline
              />
              <CustomDatePicker
                selected={endDate}
                onChange={(date) => setEndDate(date)}
                selectsEnd
                startDate={startDate}
                endDate={endDate}
                minDate={startDate}
                inline
              />
              <Button onClick={() => setDateRange({ startDate, endDate })}>
                Apply
              </Button>
            </MenuItem>
          </Menu>
          <IconButton onClick={handleThemeChange} color="inherit">
            {darkMode ? <Brightness7 style={{ color: iconColor }} /> : <Brightness4 style={{ color: iconColor }} />}
          </IconButton>
        </Box>
      </HeaderContent>
    </HeaderBar>
  );
};

export default Header;