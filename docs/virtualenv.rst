

==========
Virtualenv
==========

Virtual Python Environment or venv is a Python environment which will help you
to install different versions of Python modules in a local directory using which
you can develop and test your code without requiring to install everything
systemwide.

Installation
============

In Python3 we can use the  **venv** module to create virtual environments.

Usage
=====

We will create a directory call *virtual* inside which we will have two
different virtual environment.

The following commands will create an env called virt1.

::

    $ cd virtual
    $ python3 -m venv virt1
    $

Now we can activate the virt1 environment.

::

    $ source virt1/bin/activate
    (virt1)[user@host]$

The first part of the prompt is now the name of the virtual environment, it
will help you identify which environment you are in when you have multiple
environments.

To deactivate the environment use *deactivate* command.

::

    (virt1)$ deactivate
    $

So, now we will install a Python module called redis.

::

    (virt1)$ pip install redis
    Collecting redis
      Downloading redis-2.10.5-py2.py3-none-any.whl (60kB)
        100% |████████████████████████████████| 61kB 607kB/s 
    Installing collected packages: redis
    Successfully installed redis-2.10.5


Now we will create another virtual environment *virt2* where we will
install the same redis module but an old 2.4 version of it.

::

    $ python3 -m venv virt2
    $ source virt2/bin/activate
    (virt2)$
    (virt2)$ pip install redis==2.4
    Downloading/unpacking redis
    Downloading redis-2.4.0.tar.gz
    Running setup.py egg_info for package redis
    Installing collected packages: redis
    Running setup.py install for redis
    Successfully installed redis
    Cleaning up...

This way you can have many different environments for all of your development
needs.

.. note:: Always remember to create virtualenvs while developing new applications. This will help you keep the system modules clean.


Pipenv
=======

`Pipenv <https://docs.pipenv.org/>`_ is a tool created by `Kenneth Reitz
<https://www.kennethreitz.org/>`_ which helps to create, manage the
virtualenvs for your projects. It also helps to install/uninstall/update the
dependencies of your project.


Installing pipenv
------------------

We can install pipenv by the following command.

::

    $ python3 -m pip install --user pipenv


Using pipenv
-------------

You can go to your project directory, and then use the command **pipenv
install** to create a new virtualenv for you. You can also pass any module
name which *pipenv* will install on the environment.

::

    $ mkdir myproject
    $ cd myproject
    $ pipenv install requests
    Creating a virtualenv for this project…
    Using /usr/bin/python3 (3.6.5) to create virtualenv…
    ⠋Already using interpreter /usr/bin/python3
    Using base prefix '/usr'
    New python executable in /home/fedora/.local/share/virtualenvs/myproject-dbBcpQ4l/bin/python3
    Also creating executable in /home/fedora/.local/share/virtualenvs/myproject-dbBcpQ4l/bin/python
    Installing setuptools, pip, wheel...done.

    Virtualenv location: /home/fedora/.local/share/virtualenvs/myproject-dbBcpQ4l
    Creating a Pipfile for this project…
    Installing requests…
    Collecting requests
    Downloading https://files.pythonhosted.org/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl (88kB)
    Collecting chardet<3.1.0,>=3.0.2 (from requests)
    Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    Collecting idna<2.7,>=2.5 (from requests)
    Downloading https://files.pythonhosted.org/packages/27/cc/6dd9a3869f15c2edfab863b992838277279ce92663d334df9ecf5106f5c6/idna-2.6-py2.py3-none-any.whl (56kB)
    Collecting certifi>=2017.4.17 (from requests)
    Using cached https://files.pythonhosted.org/packages/7c/e6/92ad559b7192d846975fc916b65f667c7b8c3a32bea7372340bfe9a15fa5/certifi-2018.4.16-py2.py3-none-any.whl
    Collecting urllib3<1.23,>=1.21.1 (from requests)
    Downloading https://files.pythonhosted.org/packages/63/cb/6965947c13a94236f6d4b8223e21beb4d576dc72e8130bd7880f600839b8/urllib3-1.22-py2.py3-none-any.whl (132kB)
    Installing collected packages: chardet, idna, certifi, urllib3, requests
    Successfully installed certifi-2018.4.16 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

    Adding requests to Pipfile's [packages]…
    Pipfile.lock not found, creating…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    Updated Pipfile.lock (b14837)!
    Installing dependencies from Pipfile.lock (b14837)…
    🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 5/5 — 00:00:02
    To activate this project's virtualenv, run the following:
    $ pipenv shell

The above command will create a new virtualenv and then also install
*requests* module in the environment. You can then use **pipenv shell**
command to activate that environment. For our example, we will use
the following Python code in a file named *main.py*.

::

    import requests
    response = requests.get('https://httpbin.org/ip')
    print('Your IP is {0}'.format(response.json()['origin']))


::

    $ pipenv shell
    $ $ python main.py 
    Your IP is 192.168.1.2

Exiting from the virtualenv
----------------------------

You can exit from the virtualenv using **exit** command, or by pressing *Ctrl+d*.


Pipfile and Pipfile.lock
=========================

If you notice your project directory after you have used **pipenv**, you will
find two new files inside, *Pipfile* and *Pipfile.lock*. These files have been
created by the **pipenv** command. You should checkin these two files into
your version control system (say: git), so that others can create the exact
same environment of yours.

Pipfile
--------

The following is the content of our *Pipfile*. It is using the `TOML
<https://en.wikipedia.org/wiki/TOML>`_ file format.

::

    [[source]]
    verify_ssl = true
    name = "pypi"
    url = "https://pypi.python.org/simple"

    [dev-packages]

    [requires]
    python_version = "3.6.5"

    [packages]
    requests = "*"

On the top it tells which source to use to get the packages. It also mentions
the Python version required. The packages section tells us what all Python
packages we need. The string `"*"` means install the latest version available
on the package index. The exact version details of the packages are stored in
the *Pipfile.lock* file, it is in machine readable `JSON
<https://en.wikipedia.org/wiki/JSON>`_ format.

Remember to install any dependency for your project using **pipenv** comamnd,
that will automatically update your *Pipfile* and *Pipfile.lock* file. If you
have any dependency which is only required for the development, you can
install them marked as *dev-packages*. In the following example I am installing
*flake8* as development dependency.

::

    $ pipenv install --dev flake8
    $ cat Pipfile
    [[source]]
    verify_ssl = true
    name = "pypi"
    url = "https://pypi.python.org/simple"

    [dev-packages]
    "flake8" = "*"

    [requires]
    python_version = "3.6.5"

    [packages]
    requests = "*"

You can watch `this talk <https://www.youtube.com/watch?v=GBQAKldqgZs>`_ by
Kenneth from PyCon 2018 to know more about *Pipenv*.

Through out the rest of the book, we will use **pipenv** to create and manage
virtualenvs for any code.
