import jquery from 'jquery'
import '../lib/jquery.console'
window.$ = jquery
window.jquery = jquery
window.jQuery = jquery
import pyConsole from './python_console'
import pythonConsoleRestApi from './python_console_rest_api'

pythonConsoleRestApi.init()
pyConsole.init()
