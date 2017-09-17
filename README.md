# Raspberry Pi Zero Voice Controlled Relay Switch

This project demonstrates how to use Raspberry Pi Zero with a relay switch for home automation. The relay switch can be controlled remotely:
* either through a **Cayenne** dashboard
* or using an external USB microphone and a speech recognition engine. The relay switch responds to saying "light on" and "light off".

For the latter option, an open source tool **Judy** is used. Judy respects privacy and performs the speech recognition directly on Raspberry Pi without a need of an internet connection, relying on a lightweight speech-to-text engine called **PocketSphinx**.

The instructions to build this project are documented here https://github.com/salekd/rpizero_smart_camera/wiki

![](https://github.com/salekd/rpizero_relay/blob/master/relay.JPG)
