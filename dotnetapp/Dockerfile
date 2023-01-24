# Use the official Microsoft SDK base image
FROM mcr.microsoft.com/dotnet/sdk:6.0

# Publish the application
WORKDIR /src
COPY . .
RUN dotnet publish "WebApi.csproj" -o /app

# Configure environment
ENV ASPNETCORE_URLS http://+:80
EXPOSE 80

# Run the application
ENTRYPOINT ["dotnet", "/app/WebApi.dll"]