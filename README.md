# BOTJon - IRC Bot

A Python-based IRC bot designed for IRC servers with configurable server, channel, and bot identity.

## Features

- **Basic IRC Functionality**: Connects to IRC server, joins channels, responds to messages
- **Command System**: Responds to various commands with `!` prefix
- **Logging**: Comprehensive logging to both file and console
- **Statistics**: Tracks bot usage and uptime
- **Error Handling**: Robust error handling and graceful shutdown

## Commands

| Command | Description |
|---------|-------------|
| `.help` | Shows available commands |
| `.time` | Shows current date and time |
| `.ping` | Responds with "Pong!" |
| `.dice` | Rolls a 6-sided die (or custom: `.dice 2d20`) |
| `.8ball` | Magic 8-ball responses |
| `.weather` | Current weather info |
| `.weather forecast` | Weather forecast (hours/days) |
| `.joke` | Tells a random joke |
| `.stats` | Shows bot statistics and uptime |
| `.google` | Google search with top 3 results (e.g., `.google python tutorial`) |

## Installation

1. **Clone or download the project**
   ```bash
   # If you have git
   git clone <repository-url>
   cd ronbot
   ```

2. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit the .env file with your desired settings
   # IMPORTANT: Replace all placeholder values with your actual settings
   nano .env  # or use your preferred editor
   ```

4. **Make the script executable**
   ```bash
   chmod +x ronbot.py
   ```

5. **Run the bot**
   ```bash
   python3 ronbot.py
   ```

## Configuration

The bot uses environment variables for configuration. You can set these up in two ways:

### Option 1: Environment Variables (Recommended)

1. **Copy the example environment file**:
   ```bash
   cp env.example .env
   ```

2. **Edit the `.env` file** with your desired settings:
   **⚠️ IMPORTANT**: Replace all placeholder values (like `your_irc_server_here`) with your actual configuration values.
   ```bash
   # IRC Server Settings
   IRC_SERVER=your_irc_server_here
   IRC_PORT=6667
   IRC_CHANNEL=your_channel_here
   
   # Bot Identity
   BOT_NICKNAME=your_bot_nickname_here
   BOT_USERNAME=your_bot_username_here
   BOT_REALNAME=your_bot_realname_here
   
   # Optional: Weather API Key
   # WEATHER_API_KEY=your_openweathermap_api_key_here
   ```

### Option 2: Direct Code Modification

To modify these settings directly in code, edit the `RonBOT` class initialization in `ronbot.py`:

 ```python
 bot = RonBOT(
     server="your_irc_server_here",
     port=6667,
     channel="your_channel_here",
     nickname="your_bot_nickname_here",
     username="your_bot_username_here",
     realname="your_bot_realname_here"
 )
 ```

### Available Configuration Options

| Environment Variable | Default Value | Description |
|---------------------|---------------|-------------|
| `IRC_SERVER` | `your_irc_server_here` | IRC server address |
| `IRC_PORT` | `6667` | IRC server port |
| `IRC_CHANNEL` | `your_channel_here` | Channel to join |
| `BOT_NICKNAME` | `your_bot_nickname_here` | Bot's nickname |
| `BOT_USERNAME` | `your_bot_username_here` | Bot's username |
| `BOT_REALNAME` | `your_bot_realname_here` | Bot's real name |
| `WEATHER_API_KEY` | (none) | OpenWeatherMap API key for weather features |

### Advanced Configuration

For advanced users, you can also modify `config.py` directly to add additional configuration options. The configuration system supports:

- **Environment Variables**: Set via `.env` file (recommended)
- **Config File**: Direct modification of `config.py`
- **Runtime Parameters**: Pass values directly to the `RonBOT()` constructor

The system will use values in this priority order:
1. Runtime parameters (passed to constructor)
2. Environment variables (from `.env` file)
3. Default values (in `config.py`)

## Usage

1. **Start the bot**:
   ```bash
   python3 ronbot.py
   ```

2. **Join your configured channel** on your configured IRC server

3. **Use commands** in the channel:
   - Type `.help` to see all available commands
   - Try `.dice 2d20` for custom dice rolls
   - Use `.8ball` for fortune telling
   - Check `.stats` for bot information
   - Use `.google <search term>` for Google searches
   - Use `.weather <city>` for current weather
   - Use `.weather <city> forecast <hours/days>` for forecasts

4. **Weather Examples:**
   - `.weather London` - Current weather
   - `.weather London forecast 5 hours` - 5-hour forecast
   - `.weather London forecast 3 days` - 3-day forecast

5. **Auto-link detection** - Link detection temporarily disabled (will be re-enabled later)

## Logging

The bot creates a log file `ronbot.log` with detailed information about:
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
- Check if your configured IRC server is accessible
- Verify your configured channel exists
- Check your `.env` file configuration

### Environment Variable Issues
- Make sure you've copied `env.example` to `.env`
- Verify the `.env` file is in the same directory as `ronbot.py`
- Check that environment variable names match exactly (case-sensitive)
- Ensure no extra spaces around the `=` sign in `.env` file

### Permission Issues
- Make sure the script is executable: `chmod +x ronbot.py`
- Check if you have write permissions for log files

### Nickname Conflicts
- The bot automatically appends a random number if the nickname is taken
- You can change the nickname in the `.env` file or code if needed

## Extending the Bot

### Adding New Commands

1. Create a new method in the `RonBOT` class:
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
- The `.env` file is automatically ignored by git to protect sensitive information
- Never commit your `.env` file to version control

## License

This project is open source. Feel free to modify and distribute.

## Support

If you encounter issues:
1. Check the log file `ronbot.log`
2. Verify your internet connection
3. Ensure the IRC server and channel are accessible
4. Check that Python 3.6+ is installed

---

**Happy IRC Botting!** 🤖 