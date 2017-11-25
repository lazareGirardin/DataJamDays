# Parlament

## Intro

The Swiss confederation provides a large amount of data spanning virtually
every aspect of the political process in Switzerland. With a convenient API
to query the proceedings of committees, councillors, parties, logs of voting sessions ...

From this massive resource we decided to study voting patterns in the Swiss
government.


## Main contribution

Our insight was that voting patterns can be considered as a recommender
system : the user-item interaction matrix is a politician-vote interaction
matrix.

The attractiveness of this method is that we get some insights "for free".
The matrix completion setting allows for vote prediction : we can guess how
likely a politician is to vote yes/no on an issue given his voting record and
the voting record of his peers.
In the matrix factorisation setting we compute a latent space representation
of the politicians and the votes : these factors can represent some higher level
characteristics, embedded within the observations. We can compute similarities
or correlations in these higher dimensional spaces to get insight on the voting
patterns.

## Resources

* [Github](https://github.com/lazareGirardin/DataJamDays)
* [Data source](http://ws-old.parlament.ch/)
* []()

## License

This work is distributed with a [GPLv3 License](https://www.gnu.org/licenses/gpl.html).

---

> Authors
> Dylan Bourgeois ([@dtsbourg])(https://twitter.com/dtsbourg)
> Lazare Girardin (@lazareGirardin)
> Louis Duvigneau (@loduv)
