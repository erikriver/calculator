import React from 'react';
import { render, screen } from '@testing-library/react';
import Keypad from './Keypad';

test('render 0 value', () => {
  const { getByText } = render(<Keypad />);
  const buttonC = getByText("C");
  expect(buttonC).toBeInTheDocument();
  
});
