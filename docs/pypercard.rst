===================================================
Simple GUI application development using PyperCard
===================================================

In this chapter we will learn about creating very simple GUI application using
[PyperCard](https://pypercard.readthedocs.io/en/latest/). PyperCard is a
HyperCard inspired Pythonic GUI framework for beginner programmers.



Installing PyperCard in a virtualenv
-------------------------------------

The first step would be installing PyperCard in a virtualenv.


::

    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install pypercard


This may take some time, and specially while building Kivy, which is a dependency.


If you see any error in building *Kivy* on your distribution, you will have to install all dependencies
on your operating system.

On Debian Buster

::

    sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev python3-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python3-dev libmtdev-dev xclip xsel libjpeg-dev mesa-common-dev



Hello World example
-------------------


.. code-block:: python
    :linenos:

    from pypercard import Card, CardApp


    card = Card("hello", text="Hello, World!", text_color="yellow")

    app = CardApp(stack=[card, ])
    app.run()


In the first line, we are importing two classes from the module. ``Card`` is
the class for every screen in our application, and ``CardApp`` is the primary
application.

.. note::

    Remember that each card in your application must have an unique name.

If you execute the code, `python3 hello.py`, you will see the following GUI
window. It does not do much, it shows the string "Hello World!" with the text
color we mentioned (Yellow).

.. figure:: img/helloworld_pyper.png


Two Cards and a button
-----------------------

::

    from pypercard import Card, CardApp


    first_card = Card(
        "first_card",
        text="Hello, World!",
        text_color="yellow",
        buttons=[{"label": "Next", "target": "byescreen"}],
    )
    card2 = Card("byescreen", text="Hack the planet!", text_color="white")

    app = CardApp(stack=[first_card, card2])
    app.run()


In this code, we have two different cards. The ``first_card`` also got a button, with a text *Next*, and the *target* as the name
of the next card to show. In this case, we are showing the card named *bye*

.. figure:: img/twocard_pyper.gif


