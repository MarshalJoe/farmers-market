# Farmer Joe's Farmer's Market!

![Austin Farmer's Market](http://austinot.com/wp-content/uploads/2016/01/Austin-Farmers-Markets-Downtown.jpg)

## Setup

Set up your config

```
cp config-example.ini config.ini
```

Build your Docker image

```
docker build -t farmers-market .
```

And you're ready to go!

## Usage

To show the help page just run the executable without any extra commands or options.

```
./cart
```

Outputs:

```
Usage: cmd.py [OPTIONS] COMMAND [ARGS]...

  Farmer's Market Help Page

Options:
  --help  Show this message and exit.

Commands:
  add     Add item(s) to cart
  deals   Show deals
  empty   Empty cart
  print   Print cart contents
  remove  Remove item(s) from cart
  shop    Show products and prices
```

You can also add the `--help` flag to any command and get more information about it, including the arguments it accepts and available options.

**Example**
```
./cart add --help
```

Outputs

```
Usage: cmd.py add [OPTIONS] ITEM

  Add item(s) to cart

Options:
  --quantity INTEGER  Number of items to add to your cart (defaults to 1)
  --help              Show this message and exit.
```

*Note: You can reference items using either their item code (AP1) or name (Apples)*

### Add item

```
./cart add <ITEM>
```

### Show deals

```
./cart deals
```

### Empty cart

```
./cart empty
```

### Print cart

```
./cart print
```

### Remove item

```
./cart remove <ITEM>
```

### Shop products

```
./cart shop
```

## Design Notes


## TODOS

 - DONE create cart.p pickle file if one doesn't exist
 - convert between product codes and names
 - make cart total two digits
 - add logging
 - make testing classes
 - increase test coverage