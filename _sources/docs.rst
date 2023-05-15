Documentacion en Python y Sphinx
================================

Python docstring
----------------

Python puede documentarse siguiendo distintos formatos. El formato que Sphinx usa por defecto es 
reST y esta basado en reStructuredText. Los otros formatos populares son Numpydoc y el Google Python 
Style Guide.

PEP 257 - Docstring Conventions

PEP 258 - Docutils Design Specification

PEP 484 - Type Hints

Numpydoc
^^^^^^^^

.. code-block:: python

    def sumif(sequence, conditional)
        """Sum the numbers in a sequence as long as they pass a
        user-provided conditional callback function.

        Parameters
        ----------
        sequence : `list` [`float`]
            A sequence (`list`, for example) of numbers.
        conditional : callable
            A callback function that takes a single number as an
            argument. The ``conditional`` function returns `True`
            if the number passes the conditional, and `False`
            otherwise.

        Returns
        -------
        sum : `float`
            The sum of numbers that meet the conditional.

        Raises
        ------
        KeyError
            when a key error
        OtherError
            when an other error
        """
        ...


.. code-block:: python

    MAX_VALUE = 10
    """Maximum value (`int`).
    """

    class SomeClass(object):
        """Summary of SomeClass.

        Parameters
        ----------
        a : `str`
            Documentation for the ``a`` parameter.

        Raises
        ------
        ValueError
            Raised when theres a value error

        See Also
        --------
        OtherClass

        Notes
        -----
        [...]
        """

        a = None
        """Documentation for `a` (`str`)
        """ 

        def __init__(self, a):
            pass
        
        @property
        def wet(self):
            """The wet property (`bool`).
            """
            ...

        @quantity.setter
        def wet(self, q):
            ...

        @property
        def damp(self):
            """The damp property (`bool`, read-only).
            """
            ...

        def some_method(self, b):
            """Summary of method.

            Parameters
            ----------
            b : `str`
                Description of b.

            Returns
            -------
            some_value: `int`
                Description of some_value
            """
            pass

El metodo ``__init__`` nunca tiene docstring porque el constructor se documenta en el docstring de 
la clase.

Google Python Style Guide
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def sumif(sequence, conditional)
        """Sum the numbers in a sequence as long as they pass a
        user-provided conditional callback function.

        Args:
            sequence (list): A sequence of numbers.
            conditional (callable): A callback function that takes a
              single number as an argument. The ``conditional`` function
              returns `True` if the number passes the conditional, and
              `False` otherwise.

        Returns:
            int: The sum of numbers that meet the conditional.

        Raises:
            KeyError: when a key error
            OtherError: when an other error
        """
        ...


.. code-block:: python

    MAX_VALUE = 10
    """int: Maximum value.
    """

    class SomeClass(object):
        """Summary of SomeClass.

        Attributes:
            a (str): Documentation for `a`.
        
        Raises:
            ValueError: Raised when theres a value error.

        Note:
            [...]
        """

        a = None
        """Documentation for `a` (`str`)
        """ 

        def __init__(self, a):
            """Initializes the instance based on a.

            Args:
                a (str): Defines if instance exhibits this preference.
            """
        
        @property
        def wet(self):
            """bool: The wet property.
            """
            ...

        @quantity.setter
        def wet(self, q):
            ...

        @property
        def damp(self):
            """bool: The damp property.
            """
            ...

        def some_method(self, b):
            """Summary of method.

            Args:
                b (str): Description of b.

            Returns:
                int: Description of some_value.
            """
            pass

El metodo ``__init__`` puede documentarse en el docstring de la clase o en el docstring del metodo. 
Como ambas formas son aceptables, lo importante es ser consistente.

Configurar Sphinx
-----------------

Documentacion de modulos
^^^^^^^^^^^^^^^^^^^^^^^^

Se usa 'sphinx.ext.napoleon' para generar documentacion de modulos a partir del docstring del codigo.
Despues de preparar Sphinx para la documentacion, se debe habilitar la extension en el 
archivo conf.py::
    
    # conf.py 
    extensions = ['sphinx.ext.napoleon']

Usar sphinx-apidoc para el build de la documentacion::

    $ sphinx-apidoc -f -o docs/source drinks

Esto genera un archivo modules.rst y un drinks.rst. Se debe hacer referencia a module.rst en algun
archivo o en compilacion habra un warning.

Una alternativa a este ultimo comando es usar la extension 'autoapi.extension'.
Para instalarla se debe ejecutar::

    $ pip install sphinx-apidoc

Luego se debe habilitar la extension en el archivo conf.py::
    
    # conf.py 
    extensions = ['sphinx.ext.napoleon', 'autoapi.extension']

Si bien la configuracion por defecto puede ser aceptable, las modificaciones pueden ser necesarias 
en caso de que se trabaje con otros lenguajes, o si se quiere tener mas control sobre la salida o 
contenidos. En particular, en la configuracion de esta documentacion se utiliza::

    # conf.py

    # Autoapi settings
    autoapi_type = 'python'
    autoapi_dirs = ['../../drinks']
    autoapi_file_patterns = ['*.py']
    autoapi_add_toctree_entry = False

La opcion 'autoapi_add_toctree_entry = False' es para que no agregue la documentacion de forma 
automatica al toctree. Para agregarlo al toctree se creo un archivo 'api.rst' que se agrega al 
toctree de index.rst, y el contenido de 'api.rst' es:

.. code-block:: rst
    
    API
    ===

    .. toctree::
       :maxdepth: 2

       autoapi/drinks/index

Snippets de codigo
^^^^^^^^^^^^^^^^^^

Se usa 'sphinx.ext.doctest' para agregar snippets de documentacion. Despues de agregarlo a conf.py
se puede ver algo como:

.. code-block:: rst

   >>> import drinks
   >>> tea = drinks.Tea()
   >>> tea.prepare_recipe()
   Boiling water
   Steeping the tea with water at 100.0°C
   Pour into cup
   Adding lemon


Documentacion dentro del codigo
-------------------------------

Python
