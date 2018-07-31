import React from 'react';
import {render} from 'react-dom';
import Home from './pages/container/home'
import data from './api.json'

const app = document.getElementById('home-container')
render(<Home data = {data} />, app);

