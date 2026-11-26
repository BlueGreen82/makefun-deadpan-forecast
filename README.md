# Deadpan Forecasts — Cities That Do Not Exist

[![Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/BlueGreen82/makefun-deadpan-forecast/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/BlueGreen82/makefun-deadpan-forecast/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [make.fun bounty "Deadpan Forecasts for Cities That Do Not Exist"](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c): a program that writes one absurd but believable weather forecast for a city that does not exist.

## Entry

> Tonight in Grumblewick: 3 degrees, freezing fog, and the town's 400 streetlamps take turns switching off so no one feels singled out.

133 characters. A straight-faced broadcast line: a named (invented) place, a temperature, and one concrete, deadpan detail that makes the invented place feel real.

## How it works

`main.py` writes the line, and only the line, to `/output/entry.txt`. It is fully deterministic — the same bytes on every run, no randomness, no network.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
