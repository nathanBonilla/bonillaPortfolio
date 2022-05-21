import React from 'react'

import { About, Footer, Hero, Projects } from './container';
import { Navbar } from './components';
import './App.scss';

const App = () => {
  	return (
		<div className='app'>
			<Navbar />
			<Hero />
			<Projects />
			<About />
			<Footer />
		</div>
  	);
}

export default App