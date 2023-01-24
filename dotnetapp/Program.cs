var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", () => new 
{
	Runtime = ".NET Core",
	Hostname = Environment.MachineName,
	DateTimeUtc = DateTime.UtcNow,
	Version = Environment.GetEnvironmentVariable("AppVersion") ?? "1.0.0.0"
});
app.Run();