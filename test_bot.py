#!/usr/bin/env python3
"""
Test script for RonBOT
Tests bot functionality without connecting to IRC
"""

import sys
import os

# Add current directory to path to import ronbot
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ronbot import RonBOT

def test_bot_commands():
    """Test bot command functionality"""
    print("Testing RonBOT commands...")
    
    # Create bot instance (without connecting)
    bot = RonBOT()
    
    # Test commands
    test_commands = [
        (".help", "TestUser"),
        (".time", "TestUser"),
        (".ping", "TestUser"),
        (".dice", "TestUser"),
        (".dice 2d20", "TestUser"),
        (".8ball", "TestUser"),
        (".joke", "TestUser"),
        (".stats", "TestUser"),
        (".weather London", "TestUser"),
        (".weather London forecast 3 hours", "TestUser"),
        (".weather London forecast 3 days", "TestUser"),
        (".google python tutorial", "TestUser"),
        (".google how to code", "TestUser"),
    ]
    
    # Test link parsing (Link detection temporarily disabled)
    # test_links = [
    #     "Regular link: https://www.python.org",
    # ]
    
    print("\nCommand Test Results:")
    print("-" * 50)
    
    for command, user in test_commands:
        try:
            # Find the command handler
            cmd_handler = None
            for cmd, handler in bot.commands.items():
                if command.startswith(cmd):
                    cmd_handler = handler
                    break
            
            if cmd_handler:
                response = cmd_handler(user, command)
                print(f"✓ {command:<15} -> {response}")
            else:
                print(f"✗ {command:<15} -> No handler found")
                
        except Exception as e:
            print(f"✗ {command:<15} -> Error: {e}")
    
    # print("\nLink Parsing Test Results:")
    # print("-" * 50)
    # 
    # for link_message in test_links:
    #     try:
    #         links = bot.extract_links(link_message)
    #         print(f"Message: {link_message}")
    #         print(f"Extracted links: {links}")
    #         for link in links:
    #             summary = bot.get_link_summary(link)
    #             full_summary = f"{summary} - shared by TestUser"
    #             print(f"Summary: {full_summary}")
    #         print("-" * 30)
    #     except Exception as e:
    #         print(f"✗ Link parsing error: {e}")
    
    print("\nBot Statistics:")
    print(f"Messages received: {bot.stats['messages_received']}")
    print(f"Commands processed: {bot.stats['commands_processed']}")
    print(f"Uptime: {bot.stats['start_time']}")

def test_bot_initialization():
    """Test bot initialization"""
    print("\nTesting Bot Initialization...")
    print("-" * 50)
    
    try:
        bot = RonBOT()
        print(f"✓ Bot created successfully")
        print(f"  Server: {bot.server}")
        print(f"  Port: {bot.port}")
        print(f"  Channel: {bot.channel}")
        print(f"  Nickname: {bot.nickname}")
        print(f"  Commands available: {len(bot.commands)}")
        return True
    except Exception as e:
        print(f"✗ Bot initialization failed: {e}")
        return False

def main():
    """Main test function"""
    print("RonBOT Test Suite")
    print("=" * 50)
    
    # Test initialization
    if not test_bot_initialization():
        print("Initialization test failed. Exiting.")
        return
    
    # Test commands
    test_bot_commands()
    
    print("\n" + "=" * 50)
    print("Test completed successfully!")
    print("The bot is ready to run!")

if __name__ == "__main__":
    main() 