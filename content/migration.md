title: Visualizing Interprovincial Migration
date: August 18, 2019
author: Monica
summary: So far I have experimented with [network graphs](https://monicamow.github.io/we-the-north-network-analysis-of-toronto-raptors-passes.html) to show relationships between entities. I've decided to take my data visualization a step further with the *__SANKEY PLOT__*. It's a funny word, that's for sure, but it's a plot type that helps visualize *flows* between entities. Here I look at the flow of people between provinces.

I've been trying to determine the best way to visualize data that represents flows between entities. Examples of this type of data include trade, voters and immigration. I wanted to visualize the flows of migration between provinces in Canada and I wanted the plot to be interactive. 

First I considered using [chord diagrams](https://www.d3-graph-gallery.com/chord) in D3.js but D3 has a huge learning curve (due to the control it gives you in creating graphs). I also looked at the chord diagrams provided by Plotly. However, the chord diagram for Python is super ugly and I don't know enough about Plotly (yet) to customize it. I then stumbled upon the [SANKEY PLOT](https://plot.ly/python/sankey-diagram/), which Plotly can handle quite nicely. 

The problem with the Plotly Sankey graph was that it was very hard to make it interactive. I wanted to have a dropdown menu where someone can select a province and see the immigration flows out of it into all other provinces. This led me to [Dash](https://dash.plot.ly), a Python framework for building web apps, specifically data visualization apps. I had heard about Dash from some random Twitter account but I didn't think I needed it until I talked to Sam. Sam is such a good resource. Thanks Sam. Check out [his blog](https://sampurkiss.github.io).

Anyways, enough chit chat. The chart is below.

<iframe width="750" height="650" src='https://migration-chart.herokuapp.com' frameborder="0" allowfullscreen></iframe>
