<?php

namespace App\Api\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

class HelloWorldController extends AbstractController
{

    #[Route('/hello-world', name: 'hello_world')]
    public function index(): JsonResponse
    {
        return $this->json(['message' => 'Hello World']);
    }
}