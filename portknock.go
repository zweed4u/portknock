package main

import (
	"flag"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	ipPtr := flag.String("ip", "", "a string - the machine's ip address")
	flag.Parse()
	if *ipPtr == "" {
		fmt.Println("Please specify machine address with --ip option")
		os.Exit(1)
	}

	maxPort := 65536
	fmt.Printf("Running port scan 1-%d for ip: %s\n", maxPort, *ipPtr)

	for port := 1; port <= maxPort; port++ {
		timeout := time.Second
		conn, err := net.DialTimeout("tcp", net.JoinHostPort(*ipPtr, strconv.Itoa(port)), timeout)
		if err != nil {
			if !strings.Contains(err.Error(), "connection refused") {
				// fmt.Println("Connecting error:", err)
			}
		}
		if conn != nil {
			defer conn.Close()
			fmt.Println("Discovered open port", net.JoinHostPort(*ipPtr, strconv.Itoa(port)))
		}
	}
}
