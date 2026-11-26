# Name the Robot Band

One funny name for a band made of robots, plus a few words on its hit song.
Entry for the make.fun bounty
[Name the Robot Band](https://make.fun/bounty/u-motasimfuad-name-the-robot-band-1ffc6a74).

## The entry

> The Pop-Up Ads — hit single 'Click Here to Continue' has 40 million streams and zero listeners.

## How it works

`main.py` is deterministic and offline: it writes the entry text above to
`/output/entry.txt` (95 characters, UTF-8) and prints it. No randomness,
no network, no clock — two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
