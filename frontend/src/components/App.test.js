import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('render equal button', () => {
  const { getByText } = render(<App />);
  const equalButton = getByText(/=/i);
  expect(equalButton).toBeInTheDocument();
  
});
