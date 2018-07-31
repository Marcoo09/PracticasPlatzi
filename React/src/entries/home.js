import React from 'react';
import {render} from 'react-dom';
import data from '../api.json'
import Categories from '../playlist/components/categories';
import registerServiceWorker from '../registerServiceWorker'

const app = document.getElementById('root')
render(<Categories data = {data} />, app);
registerServiceWorker()