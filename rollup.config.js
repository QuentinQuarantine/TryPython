import babel from '@rollup/plugin-babel'
import { terser } from 'rollup-plugin-terser'
import resolve from 'rollup-plugin-node-resolve'
import commonJS from 'rollup-plugin-commonjs'

const production = !process.env.ROLLUP_WATCH

export default {
  input: 'TryPython/core/static/js/src/index.js',
  output: {
    file: 'TryPython/core/static/js/dist/scripts.js',
    format: 'iife',
  },
  plugins: [
    resolve(),
    commonJS({
      include: 'node_modules/**',
    }),
    babel({ babelHelpers: 'bundled' }),
    production && terser(),
  ],
}
