using Avalonia;
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Interactivity;
using NoNameMusicApp.ViewModels;

namespace NoNameMusicApp.Views;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        StartTabs();
        DataContext = new MainWindowViewModel();
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
    private void ChangeToDetailsClick(object sender,RoutedEventArgs e)
    {
        DetailsGrid.IsVisible = true;
        LibraryGrid.IsVisible = false;
        DiskGrid.IsVisible = false;
    }
    private void ChangeToLibraryClick(object sender,RoutedEventArgs e)
    {
        DetailsGrid.IsVisible = false;
        LibraryGrid.IsVisible = true;
        DiskGrid.IsVisible = false;
    }
    private void ChangeToDiskClick(object sender,RoutedEventArgs e)
    {
        DetailsGrid.IsVisible = false;
        LibraryGrid.IsVisible = false;
        DiskGrid.IsVisible = true;
    }
    private void StartTabs()
    {
        DetailsGrid.IsVisible = false;
        LibraryGrid.IsVisible = true;
        DiskGrid.IsVisible = false;
    }
    
    private void OnPlayMusicButtonClick(object sender, RoutedEventArgs e)
    {
        ((MainWindowViewModel)DataContext).PlayMusicButtonClick(sender, e);
    }
}