using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Interactivity;
using LibVLCSharp;
using LibVLCSharp.Shared;

namespace NoNameMusicApp.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
#pragma warning disable CA1822 // Mark members as static
    public string Greeting => "PlayMusicButtonClick";

    public void PlayMusicButtonClick(object sender,RoutedEventArgs e)
    {
        Console.WriteLine("Assets/musicTest/Dealer.mp3");
        LibVLCSharp.Shared.Core.Initialize();
        var lib = new LibVLC();
        var player = new MediaPlayer(lib);
        player.Media = new Media(lib,"Assets/musicTest/Dealer.mp3",FromType.FromPath);
        player.Play();
        // player.Volume = 200;
    }

#pragma warning restore CA1822 // Mark members as static
}
