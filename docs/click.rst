Building command line applications with Click
==============================================


I recommend `click <http://click.pocoo.org/>`_
module to build command line applications. Like any other project from `Armin
Ronacher <http://lucumr.pocoo.org/about/>`_, it has great documentation. In this
post, I am going to write a beginners tutorial, you should the read the
documentation for any more details and examples.


Installation, and development tips
-----------------------------------

Using virtualenv is highly recommended for developing "click" applications. I
am going to assume that we are in an empty directory and the continue from
there. To start, we will have a simple hello.py file with the following
content:

::

    def cli():
    	print("Hello World")

Now we will need a setup.py file. This will help us to use the python module we
are writing as a command line tool. It is also the recommended way to write
command line tools in python, then directly using shebang based scripts.

::

    from setuptools import setup

    setup(
        name="myhello",
        version='0.1',
        py_modules=['hello'],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            myhello=hello:cli
        ''',
    )

You can see that we mentioned the starting point of our tool in the
entry_points, *hello:cli* points to the right function to start with. We can
then install this on the virtualenv locally. I will also create the virtualenv
below so that becomes easier others. To learn more, read this
`chapter <http://click.pocoo.org/5/setuptools/#setuptools-integration>`_ later.

::

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install --editable .
    Obtaining file:///home/kdas/code/practice/yoclick
    Collecting Click (from myhello==0.1)
    Using cached click-6.7-py2.py3-none-any.whl
    Installing collected packages: Click, myhello
    Running setup.py develop for myhello
    Successfully installed Click-6.7 myhello

    $ myhello
    Hello World

Now to convert the same script into a click based tool, we will make the
following modifications. Now when we execute the command again, we see nothing
changed visually, but it magically has a *--help* command line argument (which
is optional).

::

    $ myhello 
    Hello World
    $ myhello --help
    Usage: myhello [OPTIONS]

    Options:
    --help  Show this message and exit.

### Using echo for printing text

The click module suggests using *echo* function to print, rather than the
standard print function. So, we will make the required change in our code.

::

    import click

    @click.command()
    def cli():
        click.echo("Hello World")

Boolean flags
--------------

In a command line tool, we sometimes want to have a boolean option. If the
option is provided then do something, if not provided, then do something else.
In our example, we will call the flag as *--verbose*, it is provided, then we
will print some extra text.

::

    import click

    @click.command()
    @click.option('--verbose', is_flag=True, help="Will print verbose messages.")
    def cli(verbose):
        if verbose:
            click.echo("We are in the verbose mode.")
        click.echo("Hello World")


We added another decorator to the cli function. In *click.option()* decorator,
first we passed the flag using *--verbose*, then marked this option as a
boolean flag, and then finally added the help text.

::

    $ myhello --help
    Usage: myhello [OPTIONS]

    Options:
    --verbose  Will print verbose messages.
    --help     Show this message and exit.
    $ myhello --verbose
    We are in the verbose mode.
    Hello World

By default, any boolean flag is treated as false.

### Standard options in the command line

We can now add more options to our tool. For example, we will have a *--name*
option which will take a string as input.

::

    import click

    @click.command()
    @click.option('--verbose', is_flag=True, help="Will print verbose messages.")
    @click.option('--name', default='', help='Who are you?')
    def cli(verbose,name):
        if verbose:
            click.echo("We are in the verbose mode.")
        click.echo("Hello World")
        click.echo('Bye {0}'.format(name))

::


    $ myhello --help
    Usage: myhello [OPTIONS]

    Options:
    --verbose    Will print verbose messages.
    --name TEXT  Who are you?
    --help       Show this message and exit.
    $ myhello
    Hello World
    Bye 
    $ myhello --name kushal
    Hello World
    Bye kushal


Same option multiple times
---------------------------

We may want to take the same option multiple times. Click has a very simple way to do so.

::

    import click

    @click.command()
    @click.option('--verbose', is_flag=True, help="Will print verbose messages.")
    @click.option('--name', '-n', multiple=True, default='', help='Who are you?')
    def cli(verbose,name):
        if verbose:
            click.echo("We are in the verbose mode.")
        click.echo("Hello World")
        for n in name:
            click.echo('Bye {0}'.format(n))

In the above example, you can see that we specified the *--name* as a multiple
options. It also means the name parameter in the *cli* function is now a tuple.

### Help text for the script

We can add help text for the script using python docstrings. For example:

::

    import click

    @click.command()
    @click.option('--verbose', is_flag=True, help="Will print verbose messages.")
    @click.option('--name', '-n', multiple=True, default='', help='Who are you?')
    def cli(verbose,name):
        """This is an example script to learn Click."""
        if verbose:
            click.echo("We are in the verbose mode.")
        click.echo("Hello World")
        for n in name:
            click.echo('Bye {0}'.format(n))

::

    $ myhello --help
    Usage: myhello [OPTIONS]

    This is an example script to learn Click.

    Options:
    --verbose        Will print verbose messages.
    -n, --name TEXT  Who are you?
    --help           Show this message and exit.

Super fast way to accept password with confirmation
----------------------------------------------------

Click provides a *password_option()* decorator, which can be used to accept a
password over hidden prompt and second confirmation prompt. Btw, I am printing
the password here as an example, never print the password to stdout in any
tool.

::

    import click

    @click.command()
    @click.option('--verbose', is_flag=True, help="Will print verbose messages.")
    @click.option('--name', '-n', multiple=True, default='', help='Who are you?')
    @click.password_option()
    def cli(verbose,name, password):
        """This is an example script to learn Click."""
        if verbose:
            click.echo("We are in the verbose mode.")
        click.echo("Hello World")
        for n in name:
            click.echo('Bye {0}'.format(n))
        click.echo('We received {0} as password.'.format(password))


The output looks like below:

::

    $ myhello --help
    Usage: myhello [OPTIONS]

    This is an example script to learn Click.

    Options:
    --verbose        Will print verbose messages.
    -n, --name TEXT  Who are you?
    --password TEXT
    --help           Show this message and exit.
    $ myhello
    Password: 
    Repeat for confirmation: 
    Hello World
    We received hello as password.


To learn the full usage of password prompts, read `this section <http://click.pocoo.org/5/options/#password-prompts>`_.

Must have arguments
--------------------

You can also add arguments to your tool. These are must haves, and if no
default value is provided, they are assumed to be strings. In the below
example, the script is expecting a county name to be specified.

::

    import click

    @click.command()
    @click.option('--verbose', is_flag=True, help="Will print verbose messages.")
    @click.option('--name', '-n', multiple=True, default='', help='Who are you?')
    @click.argument('country')
    def cli(verbose,name, country):
        """This is an example script to learn Click."""
        if verbose:
            click.echo("We are in the verbose mode.")
        click.echo("Hello {0}".format(country))
        for n in name:
            click.echo('Bye {0}'.format(n))

The output looks like:

::

    $ myhello
    Usage: myhello [OPTIONS] COUNTRY

    Error: Missing argument "country".
    $ myhello India
    Hello India


Click has many other useful features, like *yes parameter*, *file path input*.
I am not going to write about all of those here, but you can always from the
`upstream documentation <http://click.pocoo.org/>`_.