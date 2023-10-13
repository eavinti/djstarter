import React from 'react';
import {createRoot} from 'react-dom/client';

import Initializer from './components/Initializer';
import FirstComponent from './components/FirstComponent';

import './index.css';


function renderComponent(domId, Component, props = {}) {
    const domElement = document.getElementById(domId);
    const preloader = document.getElementById("preloader");
    if (domElement) {
        const datasetProps = Object.keys(domElement.dataset).reduce((acc, key) => {
            acc[key] = domElement.dataset[key];
            return acc;
        }, {});
        const combinedProps = {...datasetProps, ...props};
        const root = createRoot(domElement);
        root.render(<Component {...combinedProps} />);
        const preloader = document.getElementById("preloader");
    }
    setTimeout(function () {
        preloader.style.opacity = "0";
        preloader.addEventListener("transitionend", function () {
            preloader.style.display = "none";
        });
    }, 500);
}

// YOUR COMPONENTS:
renderComponent('initializer', Initializer);
renderComponent('first-component', FirstComponent);
