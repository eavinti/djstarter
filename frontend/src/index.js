import React from 'react';
import { createRoot } from 'react-dom/client';

import Initializer from './components/Initializer';
import FirstComponent from './components/FirstComponent';

import './index.css';


function renderComponent(domId, Component, props = {}) {
    const domElement = document.getElementById(domId);
    if (domElement) {
        const root = createRoot(domElement);
        root.render(<Component {...props} />);
    }
}


renderComponent('initializer', Initializer);
renderComponent('first-component', FirstComponent);
