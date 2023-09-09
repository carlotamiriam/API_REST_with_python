# API_REST_with_python


 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with watchdog (fsevents)
 * Debugger is active!


"Serving Flask app 'app' (lazy loading)": Esto indica que Flask está sirviendo la aplicación llamada 'app'. El término 'lazy loading' significa que Flask cargará la aplicación solo cuando sea necesario.

"Environment: production": Aunque este mensaje dice "production" (producción), en realidad estás ejecutando tu aplicación en un entorno de desarrollo. Flask suele emitir este mensaje para informarte que el entorno no es adecuado para una implementación de producción.

"WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.": Este es un recordatorio importante de que el servidor de desarrollo de Flask no debe utilizarse en un entorno de producción. En producción, debes utilizar un servidor WSGI (por ejemplo, Gunicorn o WSGI) para servir tu aplicación Flask.

"Debug mode: on": Indica que el modo de depuración está activado. En modo de depuración, Flask proporciona información detallada sobre errores y permite recargar automáticamente la aplicación cuando se realizan cambios en el código.

"Restarting with watchdog (fsevents)": Esto indica que Flask está utilizando un observador de cambios (watchdog) para detectar automáticamente cambios en los archivos y recargar la aplicación cuando sea necesario.

