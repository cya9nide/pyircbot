# PyIRCBot - IRC Bot

A Python-based IRC bot designed for IRC servers with configurable identity.
WIP - Weather using weatherapi.com API working.

## Available Commands

- `.weather [location]`: Get current weather information (supports city, state/country).
- `.stats`: Show bot statistics including uptime and monthly loudmouth (user with most messages in current month).
- `.topusers`: List the top 3 users who have sent the most messages in the channel for the current month.
  (search command removed)
- `.dice [number]`: Roll dice (e.g., `.dice 20` for a 20-sided die).
- `.8ball [question]`: Ask the magic 8-ball a question.
- `.joke`: Get a random joke.
- `.time`: Show current time.
- `.ping`: Test bot response time.
- `.help`: Show available commands.

## Features

- **Monthly Statistics Tracking**: The bot tracks user activity on a monthly basis, with automatic log rotation at the start of each month.
- **Loudmouth Detection**: Identifies the user with the most messages in the current month.
- **Top Users**: Shows the top 3 most active users for the current month.
- **Weather Integration**: Get current weather information for any location.
  (search integration removed)
- **Log Rotation**: Automatic monthly log archiving to keep logs organized.
- **Configurable Log Directory**: Support for custom log directory via LOG_DIR environment variable.

## Log Files

The bot creates monthly log files in the format `pyircbot_MM-YYYY.log` (e.g., `pyircbot_08-2025.log`). When a new month begins, the previous month's log is automatically archived as `pyircbot_MM-YYYY_archive.log`.

## Installation

1. **Clone or download the project**
   ```bash
   # If you have git
   git clone https://github.com/cya9nide/pyircbot
   cd pyircbot
   ```

2. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Set up environment variables (REQUIRED)**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit the .env file with your desired settings
   # IMPORTANT: Set the required values as described in env.example
   vi .env  # or use your preferred editor
   ```

4. **Make the script executable**
   ```bash
   chmod +x start_bot.sh
   ```

5. **Run the bot**
   ```bash
   ./start_bot.sh
   ```

## Configuration

The bot uses environment variables for configuration. You can set these up in two ways:

### Option 1: Environment Variables (Recommended)

1. **Copy the example environment file**:
   ```bash
   cp env.example .env
   ```

2. **Edit the `.env` file** with your desired settings. Refer to `env.example` for the list of variables. Do not commit your `.env` file.

### Option 2: Direct Code Modification

Advanced users may adjust defaults in code, but using `.env` is recommended.

### Available Configuration Options

| Environment Variable | Default Value | Description |
|---------------------|---------------|-------------|
| `BOT_NICKNAME` | (required) | Bot's nickname |
| `BOT_USERNAME` | (required) | Bot's username |
| `BOT_REALNAME` | (required) | Bot's real name |
| `LOG_DIR` | `.` | Directory for log files |
| `WEATHER_API_KEY` | (none) | WeatherAPI.com API key for weather features |

### Advanced Configuration

For advanced users, you can also modify `config.py` directly to add additional configuration options. The configuration system supports:

- **Environment Variables**: Set via `.env` file (recommended)
- **Config File**: Direct modification of `config.py`
- **Runtime Parameters**: Pass values directly to the `PyIRCBot()` constructor

The system will use values in this priority order:
1. Runtime parameters (passed to constructor)
2. Environment variables (from `.env` file)
3. Default values (in `config.py`)

## Usage

1. **Start the bot**:
   ```bash
   ./start_bot.sh
   ```

2. **Use commands** in the channel:
   - Type `.help` to see all available commands
   - Try `.dice 2d20` for custom dice rolls
   - Use `.8ball` for fortune telling
   - Check `.stats` for bot information
  (search command removed)
   - Use `.weather <city>` for current weather
   - Use `.weather <city> forecast <hours/days>` for forecasts

4. **Weather Examples:**
   - `.weather London` - Current weather
   - `.weather Hollywood FL` - City with state
   - `.weather Manchester UK` - City with country
   - `.weather London forecast 5 hours` - 5-hour forecast
   - `.weather London forecast 3 days` - 3-day forecast

5. **Auto-link detection** - Link detection temporarily disabled (will be re-enabled later)

## Logging

The bot creates a log file `pyircbot.log` with detailed information about:
- Connection status
- Messages received
- Commands processed
- Errors and exceptions

## Stopping the Bot

Press `Ctrl+C` to gracefully stop the bot. It will:
- Send a quit message to the IRC server
- Close the socket connection
- Save final statistics

## Troubleshooting

### Connection Issues
- Ensure you have internet connectivity
- Check your `.env` file configuration

### Environment Variable Issues
- Make sure you've copied `env.example` to `.env`
- Verify the `.env` file is in the same directory as `pyircbot.py`
- Check that environment variable names match exactly (case-sensitive)
- Ensure no extra spaces around the `=` sign in `.env` file

### Permission Issues
- Make sure the script is executable: `chmod +x pyircbot.py`
- Check if you have write permissions for log files

### Nickname Conflicts
- The bot automatically appends a random number if the nickname is taken
- You can change the nickname in the `.env` file or code if needed

## Extending the Bot

### Adding New Commands

1. Create a new method in the `PyIRCBot` class:
   ```python
   def cmd_newcommand(self, sender, message):
       return "Your response here"
   ```

2. Add it to the commands dictionary:
   ```python
   self.commands = {
       # ... existing commands ...
       '!newcommand': self.cmd_newcommand,
   }
   ```

### Adding External APIs

For weather, news, or other external data:

1. Install required packages:
   ```bash
   pip install requests
   ```

2. Import and use in your command:
   ```python
   import requests
   
   def cmd_weather(self, sender, message):
       # Your weather API code here
       pass
   ```

## Security Notes

- The bot only responds to commands starting with `.`
- No sensitive information is logged
- The bot doesn't store user data
- All responses are public in the channel

## License

This project is open source. Feel free to modify and distribute.

## Support

If you encounter issues:
1. Check the log file `pyircbot.log`
2. Verify your internet connection
3. Ensure the IRC server and channel are accessible
4. Check that Python 3.6+ is installed

---

**Happy IRC Botting!** 🤖 
