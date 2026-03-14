# Runelord

A Discord bot for RuneQuest.

## Usage

### Regular skill check

```
/rq check <ability> [label]
```

`ability` is a constant number or arithmetic expression.

`label` is a text description for this roll
(it appears in the result embed).


## Hosting setup

Specify `DISCORD_TOKEN` in `.env`, then:

```sh
uv run runelord
```

## Tests

```sh
uv run pytest
```
