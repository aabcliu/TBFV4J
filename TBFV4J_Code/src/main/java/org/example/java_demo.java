package org.example;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
public class java_demo {
    public static void main(String[] args) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            String url = "http://127.0.0.1:5000/aaa";
            String code = "test";
            String jsonInputString = "{\"code\":"+"\""+code+"\""+"}";
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonInputString))
                    .build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            String resu = response.body();
            System.out.println(resu);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}