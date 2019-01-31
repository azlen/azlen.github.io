---
layout: default
title: Sprite Generator
permalink: "/projects/sprite_generator/"
date: 12/2015
description: Video game sprite generator based on Dave Bollinger's Pixel Spaceships.

---
Video game sprite generator based on _Dave Bollinger's_ [_Pixel Spaceships_](http://davebollinger.org/works/pixelspaceships/).

![](/media/2015-12 sprite_generator interface.png)

## Features

* Draw template for sprite generation
* HSL color range picker
* **Frame Animation**
* X/Y mirroring

![](/media/2015-12 sprite_generator animation.gif)
_Example of animation, spaceships_

Fun program I created for sprite generation — mostly in the span of a few days. It's kind-of almost usable, just needs a bit of work to become user-friendly. The most exciting feature is the animation. For this I created a special <i>move tool</i> which lets you move a specific pixel while keeping its state.

I stopped working on this project for multiple reasons, one of which is that I could not find an adequate method to select _ranges of colours_. The inital colour system (shown in image above) involved three range sliders for hue, saturation, and lightness (HSL). There were some obvious flaws with this system, for example one cannot create a palette of purple and yellow without including blue, teal, and green. I tried to design alternate systems to specify a palette of colours, the most successful of which is shown below. There are nodes of colour which can be connected together to specify the range of colours _between_ the two nodes.

![](/media/2015-12 sprite_generator color_example.png)

## Links

[Demo](https://azlen.me/Sprite-Generator/) <i class="grey">(good luck!)</i> <br>
[Github](https://github.com/azlen/Sprite-Generator)