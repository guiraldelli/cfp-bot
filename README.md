# "Call For Papers" Bot
This *bot* has been developed as an automatic processor of *"call for papers"*
(CFP) emails received in the academic circles.

It was developed with the necessities of the
[Adaptive Technologies Lab](http://lta.poli.usp.br/) in mind by one of its
(former) students (me), not as a final product for widespread use. However,
anyone is free to try it at his/hers own risk and, even better, collaborate for
improvements on the existing code.

## License
So far, it is still licensed under
[MIT License](https://www.tldrlegal.com/l/mit). Maybe, someday, it will be
even more open.

## Acknowledgments
We make use of [Datejs](http://www.datejs.com/) library for parsing of the
several human ways of writing dates. The library is licensed under
the [MIT License](https://www.tldrlegal.com/l/mit).

## The Old Version
This repository is originally "the house" of the old version written in Python.
If you are used with GitHub and git, feel free to navigate and learn from it.
Nonetheless...

## The New Version
The current (new) version of this bot is a port of the old code from Python to
Javascript—or, more correctly,
[Google Apps Script](https://developers.google.com/apps-script/).
Why? Very simple: because the bot is totally based in Google products and so we
could use the Google Apps Script to trigger our bot automatically, moving to
Google the responsibility of maintaining our `cron` jobs. Simple like this.

### It is **not** perfect
I know it is not a perfect bot, but it does an amazing job in a very simple way.

Could I have used machine learning? Yes.

Could I have used neural network? Yes.

Could I have used Bayesian networks? Yes.

Could I have used [mechanical turks](https://en.wikipedia.org/wiki/The_Turk)?
Yes, I could.

But, believe me, it was a night (or two) project to solve a problem we had and
was making us crazy: full inbox of CFP emails.

I am very interested in using more intelligent approaches to solve this problem,
but the probability it will happen tends to **zero**.

Anyhow, your collaboration, fork or whatever is welcome! :smile:
