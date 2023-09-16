import React from 'react';
import { createRoot } from 'react-dom/client';
import FirstComponent from './components/FirstComponent';

// ReactDOM.render(<FirstComponent />, document.getElementById('first-component'));

const firstComponent = document.getElementById('first-component');
const reactRoot = createRoot(firstComponent);
reactRoot.render(<FirstComponent tab="home" />);