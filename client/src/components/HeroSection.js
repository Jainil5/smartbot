import React from 'react';
import '../App.css';
import './HeroSection.css';

function HeroSection() {
  return (
    <div className='hero-container'>
      <video src='/videos/botandmen.mp4' autoPlay loop muted />
      <h1>AI is ready to HELP</h1>
    </div>
  );
}

export default HeroSection;
