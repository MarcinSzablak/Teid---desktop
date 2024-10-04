using Avalonia;
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Interactivity;

namespace NoNameMusicApp.Views;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }
    private void DraggableAreaPointerPressed(object sender,PointerPressedEventArgs e)
    {
        if (e.GetCurrentPoint(this).Properties.IsLeftButtonPressed)
        {
            BeginMoveDrag(e);
        }
    }
    private void MinimalizeButtonClick(object sender,RoutedEventArgs e)
    {
        WindowState = WindowState.Minimized;
    }
    private void MaximalizeButtonClick(object sender,RoutedEventArgs e)
    {
        if (WindowState == WindowState.Maximized)
        {
            WindowState = WindowState.Normal;
        }
        else
        {
            WindowState = WindowState.Maximized;
        }
    }
    private void CloseButtonClick(object sender,RoutedEventArgs e)
    {
        Close();
    }
    
}