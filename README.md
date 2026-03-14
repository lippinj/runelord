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


### Resistance table

```
/rq resist <active> <passive> [label]
```

`active` and `passive` are integer characteristics.
The effective skill is `50 + (active - passive) * 5`.


## Hosting setup

Specify `DISCORD_TOKEN` in `.env`, then:

```sh
uv run runelord
```

## Tests

```sh
uv run pytest
```
