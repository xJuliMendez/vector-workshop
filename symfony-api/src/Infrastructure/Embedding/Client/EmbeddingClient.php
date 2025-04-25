<?php

namespace App\Infrastructure\Embedding\Client;

use GuzzleHttp\Client;
use Psr\Http\Message\ResponseInterface;

class EmbeddingClient
{
    private Client $client;
    
    public function __construct(private readonly string $embeddingApiUrl)
    {
        $this->client = new Client([
            'base_uri' => $this->embeddingApiUrl,
        ]);
    }

    public function post(array $payload): ResponseInterface
    {
        return $this->client->post('/embeddings', [
            'json' => $payload,
        ]);
        

    }
    
    
}
