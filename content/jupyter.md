title: I love to create more work for myself!
date: June 5, 2019
author: Monica
summary: In this post, I discuss how to install Anaconda on Mac and use Jupyter Notebooks. I mainly wanted to document them for myself in case I have to do this again.

Setting up a development environment is always a pain. My development environment was geared toward Ruby since I used to be a Rails developer. And that environment set up was a cumulative process over several months. I had somewhat of a Python development environment, as I had Anaconda 3 installed, but I forgot how to get Jupyter Notebooks up and running in Terminal. An extra layer of complexity is that I like to have shortcut commands in Terminal so I had to set those up too. I think to avoid all this one day I will just use an IDE or a virtual environment.

Anyway, here are the steps. 

## Install Anaconda (and Jupyter Notebooks)
1. Go [to the Anaconda website](https://www.anaconda.com/distribution/) and download the latest distribution for Mac.
2. Follow all the installation steps. It should install to the `/Users/<user>/anaconda3/bin/anaconda` path. If you go `which anaconda` in Terminal it will show this path.
3. Jupyter Notebooks will be installed with Anaconda in the `/Users/<user>/anaconda3/bin/jupyter-notebook` folder. 

## Create commands and aliases for bash/zsh to make Anaconda and Jupyter Notebooks run
1. Go to your ~/.bashrc file (or ~/.zshrc file in my case since I use zsh)
2. To make Anaconda executable, add `export PATH=$PATH:$HOME/anaconda3/bin` to the file. This will allow you to use the `conda` shortcut in Terminal.
3. To run Jupyter Notebooks with a simple `jupyter-notebook` command, add `alias jupyter-notebook="/Users/<user>/anaconda3/bin/jupyter-notebook"` to the file.

## Deal with this ridiculous matplotlib font cache issue
Do what [this StackOverflow post](https://stackoverflow.com/questions/35734074/problems-with-matplotlib-is-building-the-font-cache-using-fc-list-this-may-tak?rq=1) says to do.

