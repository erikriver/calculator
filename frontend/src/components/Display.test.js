import React from 'react';
import { render, screen } from '@testing-library/react';
import Display from './Display';

test('render 0 value', () => {
  const { getByText } = render(<Display />);
  const valueZero = getByText("0");
  expect(valueZero).toBeInTheDocument();
  
});
