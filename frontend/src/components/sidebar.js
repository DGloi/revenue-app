import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { CssBaseline, IconButton } from '@mui/material';
import { styled, useTheme } from '@mui/system';
import { ExpandMore, ExpandLess } from '@mui/icons-material';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import logo from '../assets/images/logo.svg';
import { getThemeColors } from '../theme';

const Logo = styled('img')`
  width: 3.125rem;
  height: auto;
  margin: 0.5rem; 
`;

const SidebarContainer = styled('div')`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 3.75rem; 
  height: 100vh;
  background-color: ${(props) => getThemeColors(props.theme.palette.mode).primary};
  transition: width 0.3s;
  overflow: hidden;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1200; /* Ensure the sidebar is on top of the header */
  &:hover {
    width: 12.5rem;
  }
`;

const SidebarContent = styled('div')`
  width: 100%;
  padding: 1rem;
  padding-bottom: 4rem;
  overflow-y: auto; /* Enables vertical scrolling */
  scrollbar-width: thin; 
  scrollbar-color: ${(props) => getThemeColors(props.theme.palette.mode).secondary} transparent; 
  &::-webkit-scrollbar {
    width: 0.5rem; 
  }
  &::-webkit-scrollbar-track {
    background: transparent;
  }
  &::-webkit-scrollbar-thumb {
    background-color: ${(props) => getThemeColors(props.theme.palette.mode).secondary};
    border-radius: 0;
    border: 0.125rem solid ${(props) => getThemeColors(props.theme.palette.mode).primary};
  }
`;

const SidebarLink = styled(Link)`
  color: inherit;
  text-decoration: none;
  display: flex;
  align-items: center;
  padding: 0.5rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  &:hover {
    background-color: rgba(128, 128, 128, 0.2);
  }
`;

const SidebarLabel = styled('span')`
  flex-grow: 1;
`;

const CaretIcon = styled('i')`
  margin-left: auto;
  transition: transform 0.3s;
  ${(props) => props.expanded && `transform: rotate(-180deg);`}
`;

const Footer = styled('div')`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0rem;
  background-color: ${(props) => getThemeColors(props.theme.palette.mode).primary};
  position: absolute;
  bottom: 0;
  width: 100%;
  transition: width 0.3s;
`;

const ExpandCollapseButton = styled(IconButton)`
  margin-top: 0.5rem; /* 8px */
  width: 100%;
  border-radius: 0; 
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
`;

const SubItemContainer = styled('div')`
  margin-left: 1rem; /* 16px */
  padding: 0.125rem 0.25rem; /* 2px 4px */
  font-size: 0.875rem; /* Reduced text size */
`;

const Sidebar = () => {
  const theme = useTheme();
  const [expandedMenus, setExpandedMenus] = useState([]);
  const [allExpanded, setAllExpanded] = useState(false);

  const handleMenuClick = (label) => {
    setExpandedMenus((prevExpandedMenus) =>
      prevExpandedMenus.includes(label)
        ? prevExpandedMenus.filter((menu) => menu !== label)
        : [...prevExpandedMenus, label]
    );
  };

  const toggleExpandCollapseAll = () => {
    if (allExpanded) {
      setExpandedMenus([]);
    } else {
      const allExpandableMenus = menuItems.filter((item) => item.items).map((item) => item.label);
      setExpandedMenus(allExpandableMenus);
    }
    setAllExpanded(!allExpanded);
  };

  const menuItems = [
    { label: 'Home', icon: 'pi pi-fw pi-home', command: () => window.location.hash = "/homepage" },
    {
      label: 'Transactions', icon: 'pi pi-fw pi-barcode', command: () => handleMenuClick('Transactions'), items: [
        { label: 'Payments', command: () => window.location.hash = "/payments" },
        { label: 'Refunds', command: () => window.location.hash = "/refunds" },
        { label: 'Chargebacks', command: () => window.location.hash = "/chargebacks" },
      ]
    },
    {
      label: 'Ledger', icon: 'pi pi-fw pi-book', command: () => handleMenuClick('Ledger'), items: [
        { label: 'Balance', command: () => window.location.hash = "/balance" },
        { label: 'Journal Entries', command: () => window.location.hash = "/refunds" },
      ]
    },
    {
      label: 'Reports', icon: 'pi pi-fw pi-file-check', command: () => handleMenuClick('Reports'), items: [
        { label: 'Billing Plans', command: () => window.location.hash = "/billing_plan" },
        { label: 'EU VAT report', command: () => window.location.hash = "/eu_vat" },
        { label: 'Timezone Discrepancy', command: () => window.location.hash = "/timezone_discrepancy" },
        { label: 'Credit Balance', command: () => window.location.hash = "/transaction_report" },
      ]
    },
    {
      label: 'Reconciliation', icon: 'pi pi-fw pi-replay', command: () => handleMenuClick('Reconciliation'), items: [
        { label: 'Status Files', command: () => window.location.hash = "/status_files" },
        { label: 'Discrepancies', command: () => window.location.hash = "/discrepancies" },
        { label: 'Completeness', command: () => window.location.hash = "/completeness" },
        { label: 'Builder', command: () => window.location.hash = "/builder" },
      ]
    },
    {
      label: 'Configuration', icon: 'pi pi-fw pi-cog', command: () => handleMenuClick('Configuration'), items: [
        { label: 'Mapping', command: () => window.location.hash = "/mapping" },
      ]
    },
  ];

  return (
    <>
      <CssBaseline />
      <SidebarContainer theme={theme}>
        <Link to="/homepage">
          <Logo src={logo} alt="Company Logo" />
        </Link>
        <SidebarContent>
          {menuItems.map((item, index) => (
            <React.Fragment key={index}>
              <SidebarLink to={item.command ? undefined : item.items ? '#' : item.command()}>
                <div onClick={item.command} style={{ display: 'flex', alignItems: 'center', width: '100%' }}>
                  <i className={item.icon} style={{ marginRight: '0.5rem' }}></i>
                  <SidebarLabel>{item.label}</SidebarLabel>
                  {item.items && <CaretIcon expanded={expandedMenus.includes(item.label)} className="pi pi-chevron-down" />}
                </div>
              </SidebarLink>
              {item.items && expandedMenus.includes(item.label) && (
                <div>
                  {item.items.map((subItem, subIndex) => (
                    <SubItemContainer key={subIndex} index={subIndex}>
                      <SidebarLink to={subItem.command()}>
                        <div style={{ display: 'flex', alignItems: 'center', width: '100%' }}>
                          <span>{subItem.label}</span>
                        </div>
                      </SidebarLink>
                    </SubItemContainer>
                  ))}
                </div>
              )}
            </React.Fragment>
          ))}
        </SidebarContent>
        <Footer theme={theme}>
          <ExpandCollapseButton onClick={toggleExpandCollapseAll} color="inherit">
            {allExpanded ? <ExpandLess /> : <ExpandMore />}
          </ExpandCollapseButton>
        </Footer>
      </SidebarContainer>
    </>
  );
};

export default Sidebar;