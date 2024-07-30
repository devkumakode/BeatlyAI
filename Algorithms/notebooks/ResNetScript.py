
        self.input_shape = input_shape
        self.output_size = output_size
        
        self.init_block = KanResInit(input_shape[0], 64, 64, 8, 3, 1)
        self.pool = nn.AvgPool1d(kernel_size=2)
        
        self.module_blocks = nn.Sequential(
            KanResModule(64, 64, 64, 50, 50, 1),
            KanResModule(64, 64, 64, 50, 50, 1),
            KanResModule(64, 64, 64, 50, 50, 1),
            KanResModule(64, 64, 64, 50, 50, 1),
            KanResModule(64, 64, 64, 50, 50, 1),
            KanResModule(64, 64, 64, 50, 50, 1),
            KanResModule(64, 64, 64, 50, 50, 1),
            KanResModule(64, 64, 64, 50, 50, 1)
        )
        
