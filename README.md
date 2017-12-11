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

Output:

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

Output:

```
Usage: cmd.py add [OPTIONS] ITEM

  Add item(s) to cart

Options:
  --quantity INTEGER  Number of items to add to your cart (defaults to 1)
  --help              Show this message and exit.
```


### Add item

```
./cart add <ITEM> --quantity=4
```

*Note: You can reference items using either their item code (AP1) or name (Apples)*

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
./cart remove <ITEM> --quantity=4
```

*Note: You can reference items using either their item code (AP1) or name (Apples)*

### Show products

```
./cart shop
```

## Testing

Ensure `tox` is installed and run the basic command:

```
tox
```

*Note: There's more about my decision to use tox and keep it seperate from the Dockerfile in the Design Notes section under Testing*

## Design Notes

### Tracking Cart State

I wanted a solution for tracking the contents of your shopping cart so that the program..  
    1. wouldn't need to be one long interactive session.  
    2. could keep track of contents even if it exited because of an error.  
For that I decided to use [pickle](https://docs.python.org/3/library/pickle.html), a standard-library object serializer that writes objects to a binary flat file.  
For such a simple implementation, it's a lightweight, thin solution that doesn't require the management of a proper DB, but for a multi-cart version of this program, I would strongly recommend moving to a more robust solution.

### Building the CLI

Rather than parse `args` directly, I wanted to use a library that would give me a lot of the basics of a CLI for free. With [click](http://click.pocoo.org/5/) I receive:  
    1. Generated `--help` messages for both the CLI as a whole and individual commands, parameters, and options.  
    2. CLI-specific errors like `BadParameter` that fit within the CLI message structure.  
    3. A simple, declarative syntax that means I can have a concise `cmd.py` entrypoint to the larger app, where all the commands are laid out and easily reasoned through.  

### Testing

I chose `tox` and `nose` to support the testing environment. `tox` is a great testing runner that [plays well with CI / CD pipelines (like Circle CI)](https://circleci.com/docs/1.0/language-python/) and could be used to expand the current app's testing regimen to include any number of Python versions. `nose` is a library I like to use for general Python testing because it supports the usual test discovery protocols and expands the functionality of Python's built-in testing library. I try to err on the side of using the standard library -- or in this case, something that tracks very close to it -- because of the improved stability of the resulting code.

**Note**: I separated the requirements into `requirements.txt` and `requirements-dev.txt` so as to avoid installing development dependencies in the production Docker image. I felt it was acceptable to have `tox` as a standalone, separate, un-containerized dependency as a consequence of this decision because it would be available in whatever Circle CI instance was running the integration tests, as well as most developer machines.

### Credentials / Config

As someone who writes a lot of PHP and Python, I'm drawn to using `.ini` files for their cross compatibilty. They provide a means of structuring credentials for multiple services in a single file that can be used in a polygot environment.

## Conclusion

```
.___________. __    __       ___      .__   __.  __  ___    ____    ____  ______    __    __   __  
|           ||  |  |  |     /   \     |  \ |  | |  |/  /    \   \  /   / /  __  \  |  |  |  | |  | 
`---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /      \   \/   / |  |  |  | |  |  |  | |  | 
    |  |     |   __   |   /  /_\  \   |  . `  | |    <        \_    _/  |  |  |  | |  |  |  | |  | 
    |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \         |  |    |  `--'  | |  `--'  | |__| 
    |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\        |__|     \______/   \______/  (__) 

```

Thank you for your time. Please let me know if I can provide you with any more information or clarify any of the design decisions I've made in the construction of this app. I'm excited about the possibility of moving forward with Object Rocket and hope to chat with you soon.

--Joe